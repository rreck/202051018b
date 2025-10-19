```json
{
  "id": "2bd7818c4a2705ac",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293777,
  "host_pid": "9e6742732c60:1",
  "hash": "e2821cad0e39725ffa9d085eedbb1427a24ca15e8d7b1d8bc70e79a5a2c320aa",
  "cid": "QmV1e2821cad0e39725ffa9d085eedbb1427a24ca15e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293777,
      "method": "automated_fraud_detection",
      "vc_type": "VerifiableCredential"
    },
    "ucon": {
      "usage_constraints": [
        "no_pii_export",
        "audit_required"
      ],
      "purpose": "fraud_detection_analysis",
      "enforcement": "mandatory"
    },
    "eval": {
      "confidence": 1.0,
      "evidence_count": 0,
      "review_status": "pending",
      "evaluated_at": 1760293777
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_critical"
  ],
  "sig": "3c4aeb60468fe25b8a1bf97434759a20752a410b50d5df8f069e78669481f3b0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000240631421
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 225, 'threshold': 50, 'total_amount': 32818725, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 224, 'first_seen': 1760285763, 'matching_hash': 'a12eb13bd276459e'}}}
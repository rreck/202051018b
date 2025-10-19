```json
{
  "id": "7c38153cbd8b64bb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289606,
  "host_pid": "9e6742732c60:1",
  "hash": "d1e48498e8211136a45625856f1219cd49b7f5ba7ab80f36653a769144f6842d",
  "cid": "QmV1d1e48498e8211136a45625856f1219cd49b7f5ba",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289606,
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
      "evaluated_at": 1760289606
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
  "sig": "8b65a8ac90c1108f6c9b9b510ab96ea7b0182982131a1dd26c7cdbeb03c11261"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000027747327
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 128, 'threshold': 50, 'total_amount': 41773824, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 127, 'first_seen': 1760285763, 'matching_hash': 'bf09531d82abcda7'}}}
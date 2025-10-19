```json
{
  "id": "8dd3bc5225bb375b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294035,
  "host_pid": "9e6742732c60:1",
  "hash": "8d4864b29b723f4b4f29f97d0b9b0bdf5d8e6c2025759b9e54d33ad3d74a9043",
  "cid": "QmV18d4864b29b723f4b4f29f97d0b9b0bdf5d8e6c20",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294035,
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
      "evaluated_at": 1760294035
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
  "sig": "ba6e26e13414c9e93a9c0bb3f0cdd1d2e5e9bb27f708b069f477160b45037017"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100271648434
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 230, 'threshold': 50, 'total_amount': 54441690, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 229, 'first_seen': 1760285763, 'matching_hash': '7a167e1c4ddc5d6e'}}}
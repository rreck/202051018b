```json
{
  "id": "3ba7d0f73d51bb90",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292556,
  "host_pid": "9e6742732c60:1",
  "hash": "29abb5cd4118fd53832997f7a158dbd6b9c22c7c7a26b84c810d88fab0d7fcac",
  "cid": "QmV129abb5cd4118fd53832997f7a158dbd6b9c22c7c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292556,
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
      "evaluated_at": 1760292556
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
  "sig": "65e8b568b5fd6e3c4b79ddc67fcc7ec2887497781fe7535bdf5b23a6841c7203"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000029354583
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 200, 'threshold': 50, 'total_amount': 15867600, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 199, 'first_seen': 1760285763, 'matching_hash': 'dbced9ae96be05e0'}}}
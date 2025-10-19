```json
{
  "id": "8cfe92de90f9df04",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292736,
  "host_pid": "9e6742732c60:1",
  "hash": "a43a0f878f1fb1db3e066b1f04c12c594f15d21cae4aba6461f9676dfbfe42d2",
  "cid": "QmV1a43a0f878f1fb1db3e066b1f04c12c594f15d21c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292736,
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
      "evaluated_at": 1760292736
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
  "sig": "e36f77b487ce64eed05f2ee3c228e7fb160be6012929cbbc012b9b601e158b20"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000033971595
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 204, 'threshold': 50, 'total_amount': 91619664, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 203, 'first_seen': 1760285764, 'matching_hash': 'c20a798c67202fae'}}}
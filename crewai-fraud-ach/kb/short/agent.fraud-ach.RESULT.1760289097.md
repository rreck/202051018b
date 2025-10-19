```json
{
  "id": "721a09b3b2223c4c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289097,
  "host_pid": "9e6742732c60:1",
  "hash": "2de88cf05b97b5894e5bc9d44676cf6a1674a910bedaec62943f88b3ae91e818",
  "cid": "QmV12de88cf05b97b5894e5bc9d44676cf6a1674a910",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289097,
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
      "evaluated_at": 1760289097
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
  "sig": "b1bef393fdad6cc77f8aac32c0d9e3ba602bfeec0d188704dd3048f981d1df99"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000022785658
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 113, 'threshold': 50, 'total_amount': 45462499, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 112, 'first_seen': 1760285764, 'matching_hash': 'fafce013233f49bd'}}}
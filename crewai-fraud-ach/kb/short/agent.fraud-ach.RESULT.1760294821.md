```json
{
  "id": "26f15f08ef948eec",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294821,
  "host_pid": "9e6742732c60:1",
  "hash": "b11203d568f562c2084621a34c9b0a42812c6038b593d2dc38f96427d55897cf",
  "cid": "QmV1b11203d568f562c2084621a34c9b0a42812c6038",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294821,
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
      "evaluated_at": 1760294821
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
  "sig": "452bf8f1829a7ac2af86b266cb8f989aa26d20cfdd795ac484d47cbe2f951930"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000026472141
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 245, 'threshold': 50, 'total_amount': 50472940, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 244, 'first_seen': 1760285764, 'matching_hash': 'c34da1cfbf75ff05'}}}
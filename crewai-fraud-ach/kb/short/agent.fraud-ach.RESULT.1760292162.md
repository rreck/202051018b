```json
{
  "id": "b9ed093f965a6136",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292162,
  "host_pid": "9e6742732c60:1",
  "hash": "88c04faff6dfc6e03483b18bdd807b008cbc96e0bd15027e86b9585ad208de57",
  "cid": "QmV188c04faff6dfc6e03483b18bdd807b008cbc96e0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292162,
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
      "evaluated_at": 1760292162
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
  "sig": "169bda86fc10d951980d36b1d637d767b3278db9df5438db73690de945089ae5"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100276764543
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 191, 'threshold': 50, 'total_amount': 62648382, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 190, 'first_seen': 1760285765, 'matching_hash': '861ebf9054cc2433'}}}
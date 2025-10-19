```json
{
  "id": "577aa8f63b0ae5a7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293982,
  "host_pid": "9e6742732c60:1",
  "hash": "0cec7a140d6c2314e5fd2b2910ea182de19c73fe67e107d58cee0d20004e8075",
  "cid": "QmV10cec7a140d6c2314e5fd2b2910ea182de19c73fe",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293982,
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
      "evaluated_at": 1760293982
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
  "sig": "7bf5fca131a57ce9125e99d49b6144ebd49d53674f926d9100d6d271953b7643"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100271240415
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 229, 'threshold': 50, 'total_amount': 26947346, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 228, 'first_seen': 1760285765, 'matching_hash': '8c20097da64de4ba'}}}}
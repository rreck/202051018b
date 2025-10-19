```json
{
  "id": "893bb92bdfcb3ed1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292880,
  "host_pid": "9e6742732c60:1",
  "hash": "2ebda872f53ceb83dfef5cb199b388b1e63c75c305cc4f38d50a87b5f3e1606c",
  "cid": "QmV12ebda872f53ceb83dfef5cb199b388b1e63c75c3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292880,
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
      "evaluated_at": 1760292880
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
  "sig": "e2f7efa261af649195701c52519e69415b13ed14c7085d64f15f1607c11642e2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009591397699
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 207, 'threshold': 50, 'total_amount': 29920194, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 206, 'first_seen': 1760285764, 'matching_hash': '338c84efe55c1d97'}}}
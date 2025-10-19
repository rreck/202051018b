```json
{
  "id": "211d4c36940e1628",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287523,
  "host_pid": "9e6742732c60:1",
  "hash": "bab12cb435bfb2032b28f2e98f607bfe46973b447ca678ae90abb659d85ef4d5",
  "cid": "QmV1bab12cb435bfb2032b28f2e98f607bfe46973b44",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287523,
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
      "evaluated_at": 1760287523
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
  "sig": "a605d733da70f85ac9fe16eaabd3bd15c3f749542cafdad66e4f45254abb217d"
}
```

Fraud detected: duplicate_transaction (score: 80)
Transaction: 121000245772760
Details: {'velocity': {'fraud_detected': True, 'risk_score': 76, 'details': {'transaction_count': 63, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 62, 'first_seen': 1760285763, 'matching_hash': '6b0c370090b6c980'}}}een': 1760285765, 'matching_hash': '3595d612a0391b5c'}}}
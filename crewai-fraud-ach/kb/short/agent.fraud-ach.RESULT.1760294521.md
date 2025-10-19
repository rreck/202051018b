```json
{
  "id": "eee06c4949463903",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294521,
  "host_pid": "9e6742732c60:1",
  "hash": "8ead5fb98bac7cd6c3c364727dce01496c991fb8bd6c4babe7f30c7516c506c2",
  "cid": "QmV18ead5fb98bac7cd6c3c364727dce01496c991fb8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294521,
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
      "evaluated_at": 1760294521
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
  "sig": "aa92819f490eadb8b539625cde70c4a5ce6c7fe6bc0262cb496cd36e124eec93"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105151363741
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 239, 'threshold': 50, 'total_amount': 103587141, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 238, 'first_seen': 1760285765, 'matching_hash': 'ec824383c23ded7d'}}}
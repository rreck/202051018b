```json
{
  "id": "3f2397da604491a9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294716,
  "host_pid": "9e6742732c60:1",
  "hash": "44214b7fad8e5df3ca0c5fe56f14de37a30ff7500945438a32e3856d053eca9a",
  "cid": "QmV144214b7fad8e5df3ca0c5fe56f14de37a30ff750",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294716,
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
      "evaluated_at": 1760294716
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
  "sig": "3c8729d789a6eb7c603285a52837f7a8bccdcbbfa9468bc7a9958caec65be4b7"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009597863146
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 243, 'threshold': 50, 'total_amount': 21829419, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 242, 'first_seen': 1760285763, 'matching_hash': '4ed1fbb19cfa36d6'}}}
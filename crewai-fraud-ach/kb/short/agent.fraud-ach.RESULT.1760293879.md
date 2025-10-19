```json
{
  "id": "310003e71a5390a6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293879,
  "host_pid": "9e6742732c60:1",
  "hash": "5c3454d9717d92321a56118996b83d2bc7b16e69d238aa1e4efb6083adada578",
  "cid": "QmV15c3454d9717d92321a56118996b83d2bc7b16e69",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293879,
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
      "evaluated_at": 1760293879
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
  "sig": "87550b0183c3338821fa154c3b787de6ca54217250cedf71efa7bc63dd738ccc"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009598847454
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 227, 'threshold': 50, 'total_amount': 78712704, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 226, 'first_seen': 1760285763, 'matching_hash': '71a427f0fcb5a05e'}}}
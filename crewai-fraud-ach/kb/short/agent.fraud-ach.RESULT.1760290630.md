```json
{
  "id": "769640a42e8fa3f3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290630,
  "host_pid": "9e6742732c60:1",
  "hash": "c4544234c4ee83a8717328ab1af63df008120db3247412e8c778895959801beb",
  "cid": "QmV1c4544234c4ee83a8717328ab1af63df008120db3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290630,
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
      "evaluated_at": 1760290630
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
  "sig": "1f9908b01ae9a8ac9d7d818f58784b46371a6d6e688c77625d3cb47731d8f323"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000029163318
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 155, 'threshold': 50, 'total_amount': 47810835, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 154, 'first_seen': 1760285765, 'matching_hash': 'b5567c8565e47211'}}}
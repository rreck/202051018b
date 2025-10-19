```json
{
  "id": "1873f8801c7b6f7a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293768,
  "host_pid": "9e6742732c60:1",
  "hash": "25b18bf6f079055ab7e07e1a77466adb2f75361db307b26397879338c969acf0",
  "cid": "QmV125b18bf6f079055ab7e07e1a77466adb2f75361d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293768,
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
      "evaluated_at": 1760293768
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
  "sig": "c1f5dc31574fa043c58c34770e13bfab5fc5abe29b6994be047efc7f40e5bb87"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000024421000
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 225, 'threshold': 50, 'total_amount': 101770875, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 224, 'first_seen': 1760285763, 'matching_hash': 'ab9abea401ffdb4a'}}}
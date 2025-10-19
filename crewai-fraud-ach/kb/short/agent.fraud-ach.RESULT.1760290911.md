```json
{
  "id": "a6f79da2e99d7645",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290911,
  "host_pid": "9e6742732c60:1",
  "hash": "58fce996e6c3845fc35fb48acbc9de77e6e7f3ae03031f077cdc864cbe1b23de",
  "cid": "QmV158fce996e6c3845fc35fb48acbc9de77e6e7f3ae",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290911,
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
      "evaluated_at": 1760290911
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
  "sig": "f0d09bb3dd058a6b93bb0ceea0aeaa9c4d958a4e9665de85a2f077aa109efc1b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000023479394
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 162, 'threshold': 50, 'total_amount': 63694512, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 161, 'first_seen': 1760285763, 'matching_hash': '601e7e272d8441f2'}}}
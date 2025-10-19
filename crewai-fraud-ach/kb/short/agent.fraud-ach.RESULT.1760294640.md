```json
{
  "id": "20fa2dadf9cbcb89",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294640,
  "host_pid": "9e6742732c60:1",
  "hash": "465100be200adb2f03f0a7d81f698839c364ae7a361cbd623bc13bc15bfc98e4",
  "cid": "QmV1465100be200adb2f03f0a7d81f698839c364ae7a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294640,
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
      "evaluated_at": 1760294640
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
  "sig": "4d8db03e555cbccfd4100937f0a3f47d1757773875515bdf5e4e225cd28cab47"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009593711895
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 242, 'threshold': 50, 'total_amount': 94446792, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 241, 'first_seen': 1760285763, 'matching_hash': '1e7ea83d54912238'}}}}
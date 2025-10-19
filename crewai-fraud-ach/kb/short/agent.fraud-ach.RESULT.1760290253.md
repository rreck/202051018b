```json
{
  "id": "293dab356cde0dae",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290253,
  "host_pid": "9e6742732c60:1",
  "hash": "d64d908173a2f2fdb8b7ff3edd4b48524d961e871e168a2853881278cdfe7432",
  "cid": "QmV1d64d908173a2f2fdb8b7ff3edd4b48524d961e87",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290253,
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
      "evaluated_at": 1760290253
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
  "sig": "dce483f4700add2c4280dc7b2ad4e4c35f4965ce9592a4e561f9fb8776ba7432"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000024542500
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 145, 'threshold': 50, 'total_amount': 62836910, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 144, 'first_seen': 1760285765, 'matching_hash': 'f616428a070fc3ba'}}}
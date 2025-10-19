```json
{
  "id": "8dcf43b6a5bde272",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290708,
  "host_pid": "9e6742732c60:1",
  "hash": "0c39229dbed6df4d62941ca7d0abd8bfee4ac05b046b0b5df16e7ce356e10e23",
  "cid": "QmV10c39229dbed6df4d62941ca7d0abd8bfee4ac05b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290708,
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
      "evaluated_at": 1760290708
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
  "sig": "4ec5c8e53f11907b07ef9946896240916f06131051fe2b447b3129a88ef0252c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100275531952
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 233, 'threshold': 50, 'total_amount': 26072700, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 232, 'first_seen': 1760284979, 'matching_hash': '283eac5c65a068f4'}}}
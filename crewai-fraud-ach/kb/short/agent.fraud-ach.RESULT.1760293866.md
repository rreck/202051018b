```json
{
  "id": "096a8ce980aaee8b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293866,
  "host_pid": "9e6742732c60:1",
  "hash": "c06af87246461bfec1bdb513d94b52a97afae98ca70c7311d340c5a5dd7d957c",
  "cid": "QmV1c06af87246461bfec1bdb513d94b52a97afae98c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293866,
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
      "evaluated_at": 1760293866
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
  "sig": "d733c8392099af24a9120a3730901287104ac771a9849382f34824845c18dd5a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000244210031
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 227, 'threshold': 50, 'total_amount': 92488653, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 226, 'first_seen': 1760285764, 'matching_hash': '572834c9990ead18'}}}
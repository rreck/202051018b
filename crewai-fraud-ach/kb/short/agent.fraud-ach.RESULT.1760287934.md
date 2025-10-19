```json
{
  "id": "d36cd7833a445b43",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287934,
  "host_pid": "9e6742732c60:1",
  "hash": "aaab414cedbfc850b81174cfd492154f93cfa244734bbbb77fad12e6b5df9d67",
  "cid": "QmV1aaab414cedbfc850b81174cfd492154f93cfa244",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287934,
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
      "evaluated_at": 1760287934
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
  "sig": "882cf96cf7841a46591b261200716e97fcec6b8438a3600da0bc8dbecef12e6b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105158912506
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 77, 'threshold': 50, 'total_amount': 11847297, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 76, 'first_seen': 1760285765, 'matching_hash': 'bcd6f6796bd6b696'}}}
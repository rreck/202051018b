```json
{
  "id": "b5d64284789f7aef",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290894,
  "host_pid": "9e6742732c60:1",
  "hash": "a5748a23bb1d0dbdbedc3390e8f70b23d70b9534dba05a1569f62e1639bc074c",
  "cid": "QmV1a5748a23bb1d0dbdbedc3390e8f70b23d70b9534",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290894,
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
      "evaluated_at": 1760290894
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
  "sig": "8f6a55258c74b37bf7ef863646e46408246c0836e0bcc2c094838f66a9970c36"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000024088542
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 162, 'threshold': 50, 'total_amount': 10516230, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 161, 'first_seen': 1760285763, 'matching_hash': '45759aa393537ed9'}}}
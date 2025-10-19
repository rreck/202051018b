```json
{
  "id": "4f04ef73cb8a34ab",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290166,
  "host_pid": "9e6742732c60:1",
  "hash": "73468064b2d0f5c63e1f53ea7eb844791c21d86ae3591e6c8a989e016835a9a7",
  "cid": "QmV173468064b2d0f5c63e1f53ea7eb844791c21d86a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290166,
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
      "evaluated_at": 1760290166
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
  "sig": "deb89dc6bb8ff77e0efc439392c410b20a8fd0147886fb49bc0951ff4b4f96c4"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009592681532
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 143, 'threshold': 50, 'total_amount': 63838346, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 142, 'first_seen': 1760285763, 'matching_hash': 'd3f1f3de1345fcff'}}}}
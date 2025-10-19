```json
{
  "id": "7bd1936a06d886b9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294820,
  "host_pid": "9e6742732c60:1",
  "hash": "a2fd52adb3a45a071a2b3d6b71099c7b98a43aed6e40a3c4f509745f1a9b6e41",
  "cid": "QmV1a2fd52adb3a45a071a2b3d6b71099c7b98a43aed",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294820,
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
      "evaluated_at": 1760294820
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
  "sig": "5b9072ddd9b94385bbb2806063694db33f14318865a971761a12dc388b235a54"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000029588067
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 245, 'threshold': 50, 'total_amount': 75403650, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 244, 'first_seen': 1760285764, 'matching_hash': '5ca8480d00f733c5'}}}
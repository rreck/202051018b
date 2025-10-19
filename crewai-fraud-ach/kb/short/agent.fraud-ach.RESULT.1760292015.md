```json
{
  "id": "e1002d5c0cd66235",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292015,
  "host_pid": "9e6742732c60:1",
  "hash": "bdb50ea6047e60a361d45c5cad52bec489352c973b952414bf6d71a9ff25103e",
  "cid": "QmV1bdb50ea6047e60a361d45c5cad52bec489352c97",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292015,
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
      "evaluated_at": 1760292015
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
  "sig": "1962cc22283f2fd3074e7f9649144db024a52fdaab71a683cbd80474f49b2774"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000024587821
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 188, 'threshold': 50, 'total_amount': 81143808, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 187, 'first_seen': 1760285765, 'matching_hash': 'e3fd1743fc412dec'}}}}
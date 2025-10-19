```json
{
  "id": "152e898c9483da0c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292783,
  "host_pid": "9e6742732c60:1",
  "hash": "1d2fbfe7ad90b4c36ad545b4a3c29619bea2ba137f3d12562548fb2be648230f",
  "cid": "QmV11d2fbfe7ad90b4c36ad545b4a3c29619bea2ba13",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292783,
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
      "evaluated_at": 1760292783
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
  "sig": "2741542af84f5684c5990d96f6aeb3ef97f4db02339471afc0487ac05df52265"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105150546450
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 205, 'threshold': 50, 'total_amount': 95233570, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 204, 'first_seen': 1760285763, 'matching_hash': '173a3d8db8c10352'}}}
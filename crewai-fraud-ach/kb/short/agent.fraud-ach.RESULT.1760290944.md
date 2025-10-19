```json
{
  "id": "6e3aa503275309bb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290944,
  "host_pid": "9e6742732c60:1",
  "hash": "adff7faa142cccee974b6b3e48d6ead57af2f4a0eb5cc854e80faebad556330b",
  "cid": "QmV1adff7faa142cccee974b6b3e48d6ead57af2f4a0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290944,
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
      "evaluated_at": 1760290944
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
  "sig": "08f41151cab8be64667a107ce894b9c2dfe7e6314ad34ab214d780629e5b4c57"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000029233033
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 163, 'threshold': 50, 'total_amount': 67683142, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 162, 'first_seen': 1760285763, 'matching_hash': 'f6bf3c76ea3935d9'}}}
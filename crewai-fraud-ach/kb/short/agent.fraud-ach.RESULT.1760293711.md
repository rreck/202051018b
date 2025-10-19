```json
{
  "id": "de5e9c87a6c1ef0b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293711,
  "host_pid": "9e6742732c60:1",
  "hash": "a6f6c325a6dcd9674e0f940d56b93475954d72adcbf85630ab1efa54080480de",
  "cid": "QmV1a6f6c325a6dcd9674e0f940d56b93475954d72ad",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293711,
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
      "evaluated_at": 1760293711
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
  "sig": "c999d0f11d89749f2ed45494de65113b18d434395f6d1c1d18bd23a5cdbe196c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201468298709
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 224, 'threshold': 50, 'total_amount': 14109536, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 223, 'first_seen': 1760285763, 'matching_hash': '7ee51499d35b3ada'}}}}
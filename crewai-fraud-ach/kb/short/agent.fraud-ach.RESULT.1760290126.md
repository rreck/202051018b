```json
{
  "id": "888da23e847f140a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290126,
  "host_pid": "9e6742732c60:1",
  "hash": "3afe368c61beed369892820e6a7be7cc38da852952e01c96b27bb8c32dfb7362",
  "cid": "QmV13afe368c61beed369892820e6a7be7cc38da8529",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290126,
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
      "evaluated_at": 1760290126
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
  "sig": "5a7584020f372faffd53dd19347427ed77e33eca42b75b813fa85251a63dd438"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000022844283
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 218, 'threshold': 50, 'total_amount': 41065750, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 217, 'first_seen': 1760284979, 'matching_hash': '9c963f39e9fb9122'}}}
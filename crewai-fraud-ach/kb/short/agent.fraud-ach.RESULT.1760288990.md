```json
{
  "id": "3fe1ab0843dd0365",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288990,
  "host_pid": "9e6742732c60:1",
  "hash": "28096fb25fc0b7d388fde80a80a52aac0bf72cdaa13579492082b85c9e8bf95b",
  "cid": "QmV128096fb25fc0b7d388fde80a80a52aac0bf72cda",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288990,
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
      "evaluated_at": 1760288990
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
  "sig": "dbba6d5624ac01767589b9acdf90200e8080c2dc206d8969d0d6c29df0332f03"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000246900677
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 186, 'threshold': 50, 'total_amount': 80802492, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 185, 'first_seen': 1760284979, 'matching_hash': '3c9e668125e5b467'}}}
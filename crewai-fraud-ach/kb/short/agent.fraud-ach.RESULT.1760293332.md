```json
{
  "id": "2083b4b6210995e2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293332,
  "host_pid": "9e6742732c60:1",
  "hash": "5b75dc6ae2d9f01807bfbf2960fb18c3c2c93b85d550ac9ebca987023d9dec85",
  "cid": "QmV15b75dc6ae2d9f01807bfbf2960fb18c3c2c93b85",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293332,
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
      "evaluated_at": 1760293332
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
  "sig": "624336790d22096bfea420fa784ea7d28c84255a4b8212978baa21740433af7d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000027745016
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 216, 'threshold': 50, 'total_amount': 103226616, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 215, 'first_seen': 1760285765, 'matching_hash': '88a158c93e7cc45f'}}}
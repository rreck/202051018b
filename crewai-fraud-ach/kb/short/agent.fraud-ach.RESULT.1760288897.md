```json
{
  "id": "84692db8bdd99978",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288897,
  "host_pid": "9e6742732c60:1",
  "hash": "1eacd9799ec799e2d63eee697a3abaa31b17348cde79c64365f781603826a7ad",
  "cid": "QmV11eacd9799ec799e2d63eee697a3abaa31b17348c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288897,
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
      "evaluated_at": 1760288897
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
  "sig": "39bcf9628d7c804fc0cd79f9428d395a039154b94b16c9eb0b11b85998b89c05"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105159904059
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 107, 'threshold': 50, 'total_amount': 48031016, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 106, 'first_seen': 1760285764, 'matching_hash': '7ad1725ffd2dadfd'}}}
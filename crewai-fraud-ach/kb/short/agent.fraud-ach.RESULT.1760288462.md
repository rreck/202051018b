```json
{
  "id": "57187427cc8ad47f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288462,
  "host_pid": "9e6742732c60:1",
  "hash": "349e939e8a8256a663848b32e6457933cfdc9b037f1f3bbc216cf02c29309ec8",
  "cid": "QmV1349e939e8a8256a663848b32e6457933cfdc9b03",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288462,
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
      "evaluated_at": 1760288462
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
  "sig": "bfceeb930b1cc6cb34224aa9812490d117275356ffb61d6e20e34425ae97bd58"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000242680908
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 94, 'threshold': 50, 'total_amount': 32407252, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 93, 'first_seen': 1760285764, 'matching_hash': '8e78dc9e18bacaa7'}}}
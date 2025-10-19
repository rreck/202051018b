```json
{
  "id": "70b98a4e26d7ead4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287836,
  "host_pid": "9e6742732c60:1",
  "hash": "917933519076b056eb975f34bc1383e9c8eb8f559ffa51ad8f7faae38b08fa71",
  "cid": "QmV1917933519076b056eb975f34bc1383e9c8eb8f55",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287836,
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
      "evaluated_at": 1760287836
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
  "sig": "4e9489abb6a57a7b0b4c75546943e1736af2502a54d4b5e7bdeea4d108de14c9"
}
```

Fraud detected: duplicate_transaction (score: 91)
Transaction: 111000022915367
Details: {'velocity': {'fraud_detected': True, 'risk_score': 98, 'details': {'transaction_count': 74, 'threshold': 50, 'total_amount': 30766610, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 73, 'first_seen': 1760285763, 'matching_hash': '4fdfaefd2437a484'}}}
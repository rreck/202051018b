```json
{
  "id": "4a1170ef5e7f2df6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293733,
  "host_pid": "9e6742732c60:1",
  "hash": "c9c5a1c556ced6ebadeed9047ce501632d41d586ec4cea7767bce8498c68ad40",
  "cid": "QmV1c9c5a1c556ced6ebadeed9047ce501632d41d586",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293733,
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
      "evaluated_at": 1760293733
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
  "sig": "ed5043cef8a8a287c36db5429618409d933b36729305bf9e7f9aa7f73c4bd758"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000025883497
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 224, 'threshold': 50, 'total_amount': 71232896, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 223, 'first_seen': 1760285765, 'matching_hash': '8c29ee71720a2634'}}}
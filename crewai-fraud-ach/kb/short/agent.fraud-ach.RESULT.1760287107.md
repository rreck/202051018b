```json
{
  "id": "83b671e51a851ba0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287107,
  "host_pid": "9e6742732c60:1",
  "hash": "177faaff8fe7c01d8a9389dfede4e782b01787619cdedca69a54946a23862a09",
  "cid": "QmV1177faaff8fe7c01d8a9389dfede4e782b0178761",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287107,
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
      "evaluated_at": 1760287107
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "e922c6a35a2fe3b79a787b465a0cfe80aeaf43c8070b1cc253e6ab4e9ae94990"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 031201467876303
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 21006432, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 47, 'first_seen': 1760285765, 'matching_hash': 'ffdb832f59bf640d'}}}
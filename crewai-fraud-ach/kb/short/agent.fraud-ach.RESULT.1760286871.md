```json
{
  "id": "037d16a9c9504e2e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286871,
  "host_pid": "9e6742732c60:1",
  "hash": "e7bccabb3146ccfed05715b260e19c55fa7cfe20a4da7b145bf89a2290b9eb57",
  "cid": "QmV1e7bccabb3146ccfed05715b260e19c55fa7cfe20",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286871,
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
      "evaluated_at": 1760286871
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
  "sig": "07c5f93a8c75bef57349bc94abd393a4dfacd3233f24d62998bf012e30bb4a44"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 063100278613406
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 16480560, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 39, 'first_seen': 1760285765, 'matching_hash': 'bc206509fe1a9621'}}}760284979, 'matching_hash': 'f9d80f2e7cffa5ec'}}}
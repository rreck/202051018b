```json
{
  "id": "32d5fcbe1e5e17a4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286317,
  "host_pid": "9e6742732c60:1",
  "hash": "a4f7391c4bf2b2c89d7a887b82cc8406bf2606ae93ba0ac6b074e76bd369cec5",
  "cid": "QmV1a4f7391c4bf2b2c89d7a887b82cc8406bf2606ae",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286317,
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
      "evaluated_at": 1760286317
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "round_amount_pattern",
    "risk_high"
  ],
  "sig": "47da7dd489c429cb49bc7697254dd694a2687054ada387bcbeb26af8ca0fad63"
}
```

Fraud detected: round_amount_pattern (score: 65)
Transaction: 111000026431469
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 21000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 20, 'first_seen': 1760285765, 'matching_hash': '51112ae34069fd52'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}
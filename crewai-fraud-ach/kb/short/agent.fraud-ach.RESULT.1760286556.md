```json
{
  "id": "b454eb69f87531a7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286556,
  "host_pid": "9e6742732c60:1",
  "hash": "2afb980bc861ce8ac52d5bdcd7aec332ebf261dfa78db53d20f5e2a3e66feebe",
  "cid": "QmV12afb980bc861ce8ac52d5bdcd7aec332ebf261df",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286556,
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
      "evaluated_at": 1760286556
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
  "sig": "1683b5e5fb8338b563792d8f4a16e6dcd6f7096cd65d05a4a2132ce795d39be9"
}
```

Fraud detected: round_amount_pattern (score: 65)
Transaction: 121000247715779
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 29000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 28, 'first_seen': 1760285763, 'matching_hash': 'e635467487b35661'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}
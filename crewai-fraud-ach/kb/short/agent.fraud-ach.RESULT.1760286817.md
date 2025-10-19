```json
{
  "id": "a6f3878efae108dd",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286817,
  "host_pid": "9e6742732c60:1",
  "hash": "1b3a8ae8d992f84a1acee1755cd392796f5218a25c209adacf0c1f9d099bd73a",
  "cid": "QmV11b3a8ae8d992f84a1acee1755cd392796f5218a2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286817,
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
      "evaluated_at": 1760286817
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
  "sig": "f90576eb4dcb7103b638c01c86065f8eac2e27cd924dcfffee8b5a1abbba94f3"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 111000020141329
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 17953100, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 37, 'first_seen': 1760285764, 'matching_hash': '1e11ace6091d7a38'}}}
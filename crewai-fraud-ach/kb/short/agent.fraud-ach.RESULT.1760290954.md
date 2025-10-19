```json
{
  "id": "2114a68468d93c0c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290954,
  "host_pid": "9e6742732c60:1",
  "hash": "88a6ee1f5d34bcf2e7e7c1875c9c4fd183c9c0d19d63682d780849b03048f28f",
  "cid": "QmV188a6ee1f5d34bcf2e7e7c1875c9c4fd183c9c0d1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290954,
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
      "evaluated_at": 1760290954
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
  "sig": "c35eb27e75d648d4de8cd4a00f1ecfbd3cb0de8c5dfa3ca072f121d49865dae3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201469103825
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 163, 'threshold': 50, 'total_amount': 58971607, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 162, 'first_seen': 1760285764, 'matching_hash': 'e83bf56ea8077a45'}}}
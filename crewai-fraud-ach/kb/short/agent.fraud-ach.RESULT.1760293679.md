```json
{
  "id": "279e8553b0bc72a5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293679,
  "host_pid": "9e6742732c60:1",
  "hash": "3e3cb6f008f2244c9a87206e1479aa213003f67b491a77fcfa201a74f28e50ce",
  "cid": "QmV13e3cb6f008f2244c9a87206e1479aa213003f67b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293679,
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
      "evaluated_at": 1760293679
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
  "sig": "a51d31080781d641ad95ae709ca3ed6ecf7be1c02849f97716ce08f035d3af1f"
}
```

Fraud detected: round_amount_pattern (score: 75)
Transaction: 044000033820068
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 223, 'threshold': 50, 'total_amount': 111500000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 222, 'first_seen': 1760285763, 'matching_hash': 'f27958456f681c61'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}
```json
{
  "id": "ad15dcc35067d929",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290861,
  "host_pid": "9e6742732c60:1",
  "hash": "f9a9720139be95244f2926e2aac19bd095d001769c87ad86daa757b1d670c5f8",
  "cid": "QmV1f9a9720139be95244f2926e2aac19bd095d00176",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290861,
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
      "evaluated_at": 1760290861
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
  "sig": "14988889493c4749b18543778a0208bad60667cd15b111f0ee7f67575a955ecb"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000246379487
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 161, 'threshold': 50, 'total_amount': 77054117, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 160, 'first_seen': 1760285764, 'matching_hash': 'aafc2265b0403e69'}}}d_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}
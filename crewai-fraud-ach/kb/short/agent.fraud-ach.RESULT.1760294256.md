```json
{
  "id": "652e581877639fbb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294256,
  "host_pid": "9e6742732c60:1",
  "hash": "ea1c16743373b44e2ae67c550aa43f5a6f31e033eda32abec35470ca32c1e190",
  "cid": "QmV1ea1c16743373b44e2ae67c550aa43f5a6f31e033",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294256,
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
      "evaluated_at": 1760294256
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
  "sig": "9a299df2fc6414e07a71d1bb42f6f6afbff51d59ce1d955a85547559ea07f69d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000026265735
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 234, 'threshold': 50, 'total_amount': 82388592, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 233, 'first_seen': 1760285765, 'matching_hash': 'e94388ee515b2db1'}}}
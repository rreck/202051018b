```json
{
  "id": "a7cc5ae7ca29640d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294199,
  "host_pid": "9e6742732c60:1",
  "hash": "7ba2d8119adb24427c42d4ad0c973eef3c6c6a7d1e5dbd9b03f4ca1d6b48c0cc",
  "cid": "QmV17ba2d8119adb24427c42d4ad0c973eef3c6c6a7d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294199,
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
      "evaluated_at": 1760294199
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
  "sig": "274bd1723b5f49ee04cdb8aa76f62df353cece935ccd65789e65e25abd53976b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009593801655
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 233, 'threshold': 50, 'total_amount': 83601332, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 232, 'first_seen': 1760285765, 'matching_hash': '965a85028669bcfb'}}}
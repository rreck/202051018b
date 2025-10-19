```json
{
  "id": "396ba07fa8d828be",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293144,
  "host_pid": "9e6742732c60:1",
  "hash": "b48bb8769a7f6bbedb6dc4f8aedcf1343c732fd8dfba311818d27008dab6857a",
  "cid": "QmV1b48bb8769a7f6bbedb6dc4f8aedcf1343c732fd8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293144,
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
      "evaluated_at": 1760293144
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
  "sig": "6a3d3401d5328d0b989f4a35d51827e3fb9b8ae928f8d1897cc6685a0cb19429"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201464250877
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 212, 'threshold': 50, 'total_amount': 79071548, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 211, 'first_seen': 1760285765, 'matching_hash': '9a278d14d50dbff1'}}}
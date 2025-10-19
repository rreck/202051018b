```json
{
  "id": "ce0c1d108828c364",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291866,
  "host_pid": "9e6742732c60:1",
  "hash": "56087d955fdf506016a039b29deb78fdec88d0ba6efed771386ae2fba3d0847c",
  "cid": "QmV156087d955fdf506016a039b29deb78fdec88d0ba",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291866,
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
      "evaluated_at": 1760291866
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
  "sig": "a46a1b8068c0a567cde595219b670b828c075ea4a5bb39cdcf48a463f6408268"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105157761036
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 185, 'threshold': 50, 'total_amount': 14149910, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 184, 'first_seen': 1760285763, 'matching_hash': '6f087e4012bb31a6'}}}
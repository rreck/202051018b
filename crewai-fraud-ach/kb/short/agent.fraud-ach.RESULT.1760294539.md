```json
{
  "id": "3afa9487a966ab77",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294539,
  "host_pid": "9e6742732c60:1",
  "hash": "d2576e4f27a0deaaac23bd2a486ecef3d02726a2e08bd72ef1a4fb5d059311a1",
  "cid": "QmV1d2576e4f27a0deaaac23bd2a486ecef3d02726a2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294539,
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
      "evaluated_at": 1760294539
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
  "sig": "ad1cceed92daee7e4768190cdb65e16c42dcb3c00e251aa82d7dd8e90851965e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105157761036
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 240, 'threshold': 50, 'total_amount': 18356640, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 239, 'first_seen': 1760285763, 'matching_hash': '6f087e4012bb31a6'}}}}
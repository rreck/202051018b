```json
{
  "id": "82dbcac21bcc97e8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289057,
  "host_pid": "9e6742732c60:1",
  "hash": "1a8a91835eab98241c1e14bdda633ddf73940f26beb83e35a99d76d3f4804872",
  "cid": "QmV11a8a91835eab98241c1e14bdda633ddf73940f26",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289057,
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
      "evaluated_at": 1760289057
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
  "sig": "7a959954b8f911b922399fa29f273bb45f8eb0bf2e8907acad9f003d55aa2302"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000029347324
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 112, 'threshold': 50, 'total_amount': 17243408, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 111, 'first_seen': 1760285763, 'matching_hash': '03de14fe5a3852ae'}}}
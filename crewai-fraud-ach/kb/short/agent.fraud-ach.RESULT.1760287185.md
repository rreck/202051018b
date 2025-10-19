```json
{
  "id": "1376ef679d90941c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287185,
  "host_pid": "9e6742732c60:1",
  "hash": "2df880aff158b984476b958b63cabbb4eb301645a30ec925d107a360a9871dee",
  "cid": "QmV12df880aff158b984476b958b63cabbb4eb301645",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287185,
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
      "evaluated_at": 1760287185
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
  "sig": "9f4d088e09ba1b280deedaa4369008c53b94dcb13f6cfc43722f8c0e7122c82c"
}
```

Fraud detected: duplicate_transaction (score: 68)
Transaction: 031201468454923
Details: {'velocity': {'fraud_detected': True, 'risk_score': 52, 'details': {'transaction_count': 51, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 50, 'first_seen': 1760285765, 'matching_hash': '07b42bdcb312ebee'}}}een': 1760285763, 'matching_hash': 'a9820f16c3d139ec'}}}27d'}}}
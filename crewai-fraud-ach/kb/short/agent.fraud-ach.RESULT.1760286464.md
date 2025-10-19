```json
{
  "id": "3409b6ab940bc230",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286464,
  "host_pid": "9e6742732c60:1",
  "hash": "52648c6e01ee9c008ee82733fdb58558eba93f68ca8bc9fb8841456976700dd9",
  "cid": "QmV152648c6e01ee9c008ee82733fdb58558eba93f68",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286464,
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
      "evaluated_at": 1760286464
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
  "sig": "61014866691b04511a11a014453b40a48fa89ec14049d2e73591d57ec362816c"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 121000240849779
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 25, 'first_seen': 1760285763, 'matching_hash': '760b7e67ac1502b4'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '789209527', 'validation_error': 'Invalid routing number checksum'}}}
```json
{
  "id": "e63684e99f87e521",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288501,
  "host_pid": "9e6742732c60:1",
  "hash": "cef317442b9410dad1d80796b42f9f6652c678728c34d0ca18c2d4e7843593fb",
  "cid": "QmV1cef317442b9410dad1d80796b42f9f6652c67872",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288501,
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
      "evaluated_at": 1760288501
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
  "sig": "bc7d7232e337347199cdbfb40d168ca76c6b36e8f04b1b9c423cc962b8726287"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000241561723
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 95, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 94, 'first_seen': 1760285764, 'matching_hash': '61d0611cbf39c4a3'}}}
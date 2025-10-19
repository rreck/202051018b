```json
{
  "id": "c8212c49e17d71d7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293827,
  "host_pid": "9e6742732c60:1",
  "hash": "3f7bb4d3dac891229a9ea66c6ccca388732747a201f1746ee5a96589d760b834",
  "cid": "QmV13f7bb4d3dac891229a9ea66c6ccca388732747a2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293827,
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
      "evaluated_at": 1760293827
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
  "sig": "7eebb355d7a8e6edc7bd5b99ffcd5ccd3d811a4f1b81c42f95087ba4d8168be3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105155104424
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 226, 'threshold': 50, 'total_amount': 65013872, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 225, 'first_seen': 1760285763, 'matching_hash': 'b81635ada84cf521'}}}
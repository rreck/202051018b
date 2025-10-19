```json
{
  "id": "1bd5512b74df4acf",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288269,
  "host_pid": "9e6742732c60:1",
  "hash": "c56357bb5a1864d01d1b0cd2da1b5270d59a286b3b2fdd5622a2dfb67a11c300",
  "cid": "QmV1c56357bb5a1864d01d1b0cd2da1b5270d59a286b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288269,
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
      "evaluated_at": 1760288269
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
  "sig": "b3c178fc6ccf5e327327cfdaaa223a91d8d8c6731159083de31524c335ac77ab"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000240945799
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 88, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 87, 'first_seen': 1760285763, 'matching_hash': '2868277a63cf50ca'}}}5765, 'matching_hash': 'bf20bb751245cb05'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '886156735', 'validation_error': 'Invalid routing number checksum'}}}